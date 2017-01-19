#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
dICOMReaderdirectory1 = FindSource('DICOMReaderdirectory1')

# create a new 'Threshold'
threshold1 = Threshold(Input=dICOMReaderdirectory1)
threshold1.Scalars = ['POINTS', 'DICOMImage']
# show only DOSE
threshold1.ThresholdRange = [4000.0, 7622.0]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get color transfer function/color map for 'DICOMImage'
dICOMImageLUT = GetColorTransferFunction('DICOMImage')

# show data in view
threshold1Display = Show(threshold1, renderView1)
# trace defaults for the display properties.
threshold1Display.ColorArrayName = ['POINTS', 'DICOMImage']
threshold1Display.LookupTable = dICOMImageLUT
threshold1Display.OSPRayScaleArray = 'DICOMImage'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'DICOMImage'
threshold1Display.ScaleFactor = 16.62890625
threshold1Display.SelectScaleArray = 'DICOMImage'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.ScalarOpacityUnitDistance = 2.5428906602855523
threshold1Display.GaussianRadius = 8.314453125
threshold1Display.SetScaleArray = ['POINTS', 'DICOMImage']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'DICOMImage']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# Rescale transfer function
dICOMImageLUT.RescaleTransferFunction(-1024.0, 7622.0)

# get opacity transfer function/opacity map for 'DICOMImage'
dICOMImagePWF = GetOpacityTransferFunction('DICOMImage')

# Rescale transfer function
dICOMImagePWF.RescaleTransferFunction(-1024.0, 7622.0)

# hide data in view
Hide(dICOMReaderdirectory1, renderView1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [157.96071299530226, 1123.585776382758, -38.74159849936598]
renderView1.CameraFocalPoint = [164.677734375, 164.677734375, 92.25]
renderView1.CameraViewUp = [-0.11784470609179896, -0.1352151618055555, -0.9837832511605568]
renderView1.CameraParallelScale = 250.4946604176746

