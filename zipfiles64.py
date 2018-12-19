import os, zipfile

source_dir, output_filename = 'cyclegan', 'pix2pixGPU_train.zip'

zipf = zipfile.ZipFile(output_filename, 'w', allowZip64 = True)
pre_len = len(os.path.dirname(source_dir))
for parent, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
        pathfile = os.path.join(parent, filename)
        arcname = pathfile[pre_len:].strip(os.path.sep)
        zipf.write(pathfile, arcname)
zipf.close()
 
