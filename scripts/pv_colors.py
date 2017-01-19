#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get color transfer function/color map for 'DICOMImage'
dICOMImageLUT = GetColorTransferFunction('DICOMImage')

# Rescale transfer function
dICOMImageLUT.RescaleTransferFunction(200.0, 7622.0)

# get opacity transfer function/opacity map for 'DICOMImage'
dICOMImagePWF = GetOpacityTransferFunction('DICOMImage')

# Rescale transfer function
dICOMImagePWF.RescaleTransferFunction(200.0, 7622.0)

#### uncomment the following to render all views
RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
