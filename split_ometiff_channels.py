import os
import sys
import tifffile

filename = sys.argv[1]
out_dir = sys.argv[2]
prefix = sys.argv[3]

os.makedirs(out_dir, exist_ok=True)

with tifffile.TiffFile(filename) as tif:
    arr = tif.asarray()
    # Check data shape, adjust if needed
    if arr.ndim == 5:
        arr = arr[0]  # If (t, c, z, y, x), take t=0
    channels = arr.shape[0]
    for i in range(channels):
        outname = os.path.join(out_dir, f"{prefix}_ch{i+1}.tif")
        tifffile.imwrite(outname, arr[i])
        print(f"Saved {outname}")

