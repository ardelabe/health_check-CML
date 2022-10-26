sftp_client = ssh_client.open_sftp()
remote_file = sftp_client.open('remote_filename')
try:
    for line in remote_file:
        # process line
finally:
    remote_file.close()