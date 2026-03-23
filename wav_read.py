import wave,os

wf = os.environ.get('LINK')

with wave.open(wf, 'rb') as f:
    # Get sample rate (frequency)
    sample_rate = f.getframerate() 
    
    # Get sample width in bytes and convert to bit depth
    sample_width = f.getsampwidth() 
    bit_depth = sample_width * 8
    
    # Get number of channels (1 for mono, 2 for stereo)
    channels = f.getnchannels()

print(f"Sample Rate: {sample_rate} Hz")
print(f"Bit Depth: {bit_depth}-bit")
print(f"Channels: {channels}")
