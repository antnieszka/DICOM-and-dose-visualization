#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'DICOM Reader (directory)'
try:
    ct = DICOMReaderdirectory(FileName='/home/<username>/DICOM/out_dir')
except:
    print("Prosze zmodyfikowac sciezke do katalogu z plikami DICOM, nazwanego prawdopodobnie out_dir")
    raise

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
renderView1.ViewSize = [1182, 756]

# show data in view
ctDisplay = Show(ct, renderView1)
# trace defaults for the display properties.
ctDisplay.Representation = 'Outline'
ctDisplay.ColorArrayName = ['POINTS', '']
ctDisplay.OSPRayScaleArray = 'DICOMImage'
ctDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
ctDisplay.SelectOrientationVectors = 'DICOMImage'
ctDisplay.ScaleFactor = 32.935546875
ctDisplay.SelectScaleArray = 'DICOMImage'
ctDisplay.GlyphType = 'Arrow'
ctDisplay.ScalarOpacityUnitDistance = 1.5760844997113737
ctDisplay.Slice = 61

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(ctDisplay, ('POINTS', 'DICOMImage'))

# rescale color and/or opacity maps used to include current data range
ctDisplay.RescaleTransferFunctionToDataRange(True, True)

# change representation type
ctDisplay.SetRepresentationType('Volume')

# get color transfer function/color map for 'DICOMImage'
dICOMImageLUT = GetColorTransferFunction('DICOMImage')

# get opacity transfer function/opacity map for 'DICOMImage'
dICOMImagePWF = GetOpacityTransferFunction('DICOMImage')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
dICOMImageLUT.ApplyPreset('Rainbow Desaturated', True)
