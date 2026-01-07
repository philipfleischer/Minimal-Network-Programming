import socket
import threading

nickname = input("Choose a nickname: ")
if nickname == "admin":
    password = input("Enter password for admin: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55554))

stop_thread = False


def receive():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
                next_message = client.recv(1024).decode("ascii")
                if next_message == "PASSWD":
                    client.send(password.encode("ascii"))
                    if client.recv(1024).decode("ascii") == "REFUSE":
                        print("Connection was Refused! Wrong Password!")
                        stop_thread = True
                elif next_message == "BAN":
                    print("Connection refused because of BAN!")
                    client.close()
                    stop_thread = True
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        if stop_thread:
            break
        message = f"{nickname}: {input('')}"
        # skipping nickname letters + colon and space
        # /command          is thereby written in the message
        if message[len(nickname) + 2 :].startswith("/"):
            if nickname == "admin":
                if message[len(nickname) + 2 :].startswith("/kick"):
                    # We need to skip username, colon, slash and (k,i,c,k,_)
                    client.send(f"KICK {message[len(nickname) + 2+6:]}".encode("ascii"))
                elif message[len(nickname) + 2 :].startswith("/ban"):
                    # We need to skip username, colon, slash and (b, a, n,_)
                    client.send(f"BAN {message[len(nickname) + 2+5:]}".encode("ascii"))
            else:
                print("Commands can only be executed by the admin!")
        else:
            client.send(message.encode("ascii"))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
