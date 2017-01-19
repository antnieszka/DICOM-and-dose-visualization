# "DICOM + Dose" visualization

The idea was pretty simple - visualize therapeutic dose on top of patients model.
The latter could be easily done using DICOM CT images and software like
[ParaView](http://www.paraview.org/) which allows to read DICOM image series.

In this project, we focus on dose data made with TRIP98.

## Requirements

- [ParaView](http://www.paraview.org/) >= 5.2 - data analysis and visualization application
- [Python](http://python.org/)
- [pytrip](https://github.com/pytrip/pytrip) - library for Python

## Overview of my idea/solution

I assume I have some treatment plans done in TRIP98 and DICOM series of CT images.

My *pipeline* (for now) looks like this:
- Place DICOM data in directory named `ct_dicom`
- Using pytrip convert DICOM files to TRIP98 format (.ctx file with binary data and .hed with metadata part which is pretty the same in each file). This can be done like this:
`dicom2trip ct_data/ test.ctx`. Now we should have two files: `test.ctx` and `test.hed`.
- Now we can make treatment plan using TRIP98 and converted above DICOMs.
- Lets name output files from planning: `plansimplephys.dos` and `plansimplephys.hed`. This is basically a `DoseCube` with .hed file, more on topic here: [DoseCube docs](https://pytrip.readthedocs.io/en/latest/apidoc/pytrip.dos.html)
- Using pytrip - create CtxCube from DICOM files and save as `test.ctx` and `test.hed` - more can be found here: [CtxCube docs](https://pytrip.readthedocs.io/en/latest/_modules/pytrip/ctx.html#CtxCube)
- Now we merge CtxCube with DoseCube (DICOM images + dose). This step can be done using my script (merge_ct_dose.py), I'll just explain below what it does:
  1. Get input files from sys.argv (*ctx_file, dose_file, output_dir*)
  2. Load *ctx_file* as CtxCube, *dose_file* as DoseCube
  3. Add 4000 to dose values (CT data is in range -1024 to about 3000, so we move it further)
  4. Merge cubes
  5. Save result CtxCube as DICOM series in *output_dir*
- Execute this script: `python merge_ct_dose.py test.hed plansimplephys.hed out_dir`
- Now we need to load it in ParaView.
  1. Open ParaView application
  2. File->Open and select *out_dir* with result DICOM data
  3. In dialog select 'DICOM files (directory)' option
  4. A *ct.** item should appear in the pipeline browser (by default on the left)
  5. Click eye icon to show object
  6. From the properties window select Representation: *Volume*
- This is the easiest way I found, I also included some scripts with coloring and thresholding in directory `scripts`

## Observations and tips
- CT images generally use [Housenfield scale](https://en.wikipedia.org/wiki/Hounsfield_scale) - this makes filtering some parts like air, fat and bones easier. E.g. to get rid of air in ParaView select "Rescale to custom range" in coloring section of properties and set it to -999 instead of -1024. This should get most of the air out of visible view.
- As mentioned in overview section - dose values were moved to 4000+, so filtering them out is also a matter of setting custom range. Same for viewing only CT image (range below 4000, like [-1000, 3000])
- My favorite visualization method for dose is done by applying threshold with values [4000, 6000], resetting coloring to visible range and changing representation to volume. Beware, it takes some time to compute.
