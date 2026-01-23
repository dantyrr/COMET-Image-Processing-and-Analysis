# COMET Image Processing and Analysis

A workflow for analyzing microglial cells from COMET multiplexed imaging data using ImageJ and downstream single-cell analysis with CAFE.

## Overview

This repository provides an alternative to Visiopharm for microglial imaging analysis. The workflow extracts single-cell expression data from multiplexed images, enabling quantification of phenotypic markers (e.g., APOE, CD68, CD206) in individual microglia.

## Workflow

### 1. Pre-processing in QuPath/Image Software

1. Open your image of interest
2. Apply background subtraction to channels
3. Draw a rectangle around the tissue region of interest
4. Select DAPI and all background-subtracted channels
5. Export the cropped region (significantly reduces file size)

### 2. Channel Splitting

Use `split_ometiff_channels.py` to split multi-channel OME-TIFF files into individual channel TIFFs:

```bash
python split_ometiff_channels.py <input.ome.tiff> <output_directory> <prefix>
```

**Requirements:**
```bash
pip install tifffile imagecodecs
```

### 3. Microglial Segmentation in ImageJ

1. Open the Iba1 channel image
2. Adjust Brightness/Contrast (slightly oversaturated) and Apply
3. `Process > Binary > Make Binary`
4. `Process > Binary > Dilate` (repeat 2x)
5. `Process > Binary > Close`
6. `Analyze > Analyze Particles`
   - Size: 1000-Infinity (keeps only large cells, excludes debris)
   - Check "Display results" and "Add to Manager"

### 4. Measure Marker Expression

1. Open phenotypic marker images (APOE, CD68, CD206, etc.)
2. B/C adjustment is not needed for measurement
3. In ROI Manager: Select all ROIs (Shift + click to bottom)
4. Click "Measure"
5. Save the "Mean" values (MFI per cell for each marker)

### 5. Data Export

Export to CSV with:
- Cell barcode (e.g., `Y_BCAS_1_cell#`)
- Sample metadata
- Marker expression values (Mean Fluorescence Intensity)

### 6. Downstream Analysis

Run the CAFE pipeline on the exported single-cell expression data. See `Young_Stroke_Sham_Microglia_Flow_for_CAFE.ipynb` for an example analysis.

## Additional Measurements

Using the saved ROIs, you can also calculate:
- Microglial cell size/area
- Spine branch number (via skeletonization)
- Spine length

## Tips

- Exclude microglia larger than ~5000 pixels (often merged cells)
- Cell barcodes allow you to trace back to specific cells and generate images
- Keep ROI files saved to revisit individual cells later

## Files

| File | Description |
|------|-------------|
| `split_ometiff_channels.py` | Splits multi-channel OME-TIFF into individual TIFFs |
| `Young_Stroke_Sham_Microglia_Flow_for_CAFE.ipynb` | Example analysis notebook |
| `Workflow for microglial imaging.docx` | Detailed text workflow |
| `Microglial_COMET_Analysis_workflow.pptx` | Visual step-by-step guide with screenshots |
