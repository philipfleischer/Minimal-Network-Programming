from ftplib import FTP
import paramiko

# Choose protocol
MODE = "SFTP"  # "SFTP" eller "FTP"

# SFTP (Paramiko)
SFTP_HOST = "localhost"
SFTP_PORT = 2222  # Codespaces needed this
SFTP_USER = "netuser"
SFTP_PASSWORD = "SFTPSERVERPASS"


# FTP (ftplib)
FTP_HOST = "something.bplaced.net"
FTP_USER = "something"
FTP_PASSWORD = "Something123"

# For demo:
CHOICE = 3  # 1=download, 2=upload, 3=cwd+download


# SFTP client
def run_sftp():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(
        SFTP_HOST,
        port=SFTP_PORT,
        username=SFTP_USER,
        password=SFTP_PASSWORD,
        look_for_keys=False,
        allow_agent=False,
        timeout=10,
    )

    sftp = ssh.open_sftp()

    print("SFTP connected. Listing home directory:")
    print(sftp.listdir("."))

    sftp.close()
    ssh.close()


# FTP client
def run_ftp():
    with FTP(FTP_HOST) as ftp:
        ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)
        print("FTP connected:", ftp.getwelcome())

        if CHOICE == 1:
            remote = "mytest.txt"
            local = "test.txt"
            with open(local, "wb") as f:
                ftp.retrbinary(f"RETR {remote}", f.write, 1024)
            print(f"Downloaded {remote} -> {local}")

        elif CHOICE == 2:
            local = "myupload.txt"
            remote = "upload.txt"
            with open(local, "rb") as f:
                ftp.storbinary(f"STOR {remote}", f)
            print(f"Uploaded {local} -> {remote}")

        elif CHOICE == 3:
            ftp.cwd("mydir")
            remote = "otherfile.txt"
            local = "myspecialfile.txt"
            with open(local, "wb") as f:
                ftp.retrbinary(f"RETR {remote}", f.write, 1024)
            print(f"Downloaded mydir/{remote} -> {local}")

        else:
            raise ValueError("CHOICE must be 1, 2, or 3")


if __name__ == "__main__":
    if MODE.upper() == "SFTP":
        run_sftp()
    elif MODE.upper() == "FTP":
        run_ftp()
    else:
        raise ValueError("MODE must be 'SFTP' or 'FTP'")
