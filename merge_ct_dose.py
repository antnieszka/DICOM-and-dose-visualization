import pytrip as pt
from sys import argv

if len(argv) != 4:
    print("Too few arguments, required: ct_file, dose_file, out_dir")
    print("Example: python %s test.hed plansimplephys.hed out_dir" % argv[0])
    exit(1)

ct_file = argv[1]
dose_file = argv[2]
out_dir = argv[3]

# read CT scans (.ctx + .hed)
ct = pt.CtxCube()
ct.read(ct_file)
print("CT min: {0}, max: {1}".format(ct.cube.min(), ct.cube.max()))

# read treatment plan (.dos + .hed)
plan = pt.DosCube()
plan.read(dose_file)
print("Dose min: {0}, max: {1}".format(plan.cube.min(), plan.cube.max()))

# move dose outside dicom image range
plan.cube[plan.cube > 0] += 4000
print("Moved Dose min: {0}, min-with-zero-excluded: {1}, max: {2}".format(plan.cube.min(), plan.cube[plan.cube > 0].min(), plan.cube.max()))

# merge plan/dose and CT scans
res = ct + plan

# write as DICOM series in given dir
res.write_dicom(out_dir)

