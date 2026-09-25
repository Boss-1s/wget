import asyncio
import ssl
import websockets

MAGMANODE_IP = "dynamic-10.magmanode.com"
MAGMANODE_PORT = 25744
LOCAL_PORT = 8081

async def handle_client(websocket):
    try:
        # Establish raw TCP connection to Magmanode backend
        reader, writer = await asyncio.open_connection(MAGMANODE_IP, MAGMANODE_PORT)

        async def ws_to_tcp():
            async for message in websocket:
                writer.write(message)
                await writer.drain()

        async def tcp_to_ws():
            while True:
                data = await reader.read(4096)
                if not data:
                    break
                await websocket.send(data)

        await asyncio.gather(ws_to_tcp(), tcp_to_ws())
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        try:
            writer.close()
            await writer.wait_closed()
        except:
            pass

async def main():
    # Setup SSL Context for the Secure WebSocket (wss://)
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    print(f"Starting Secure Eaglercraft bridge on wss://localhost:{LOCAL_PORT}")
    print(f"Routing traffic to Magmanode backend ({MAGMANODE_IP}:{MAGMANODE_PORT})...")

    # Pass the context directly into the server parameters
    async with websockets.serve(handle_client, "0.0.0.0", LOCAL_PORT, ssl=ssl_context):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
