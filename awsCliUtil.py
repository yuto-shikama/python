import subprocess

# AWS configure確認
def aws_configure():
	stdout = subprocess.run(['aws','configure','list'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
	return stdout.decode()
	
# S3でのls実行
def aws_ls(path):
	stdout = subprocess.run(['aws','s3','ls',path], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
	return stdout.decode()

# S3でのrm実行
def aws_delete(path):
	stdout = subprocess.run(['aws','s3','rm','s3://' + path], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
	return stdout.decode()
	
# S3でのupload実行
def aws_upload(path,file):
	print("aws s3 cp " + file + " s3://" + path)
	stdout = subprocess.run(['aws','s3','cp',file,'s3://' + path], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
	return stdout.decode('cp932')
	
# S3でのcp実行
def aws_cp(fromPath,toPath):
	stdout = subprocess.run(['aws','s3','cp',fromPath,toPath], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
	return stdout.decode()