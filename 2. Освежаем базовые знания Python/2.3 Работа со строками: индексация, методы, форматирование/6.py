encrypted_message = input()
n = int(input())

for _ in range(n):
    start, end = map(int, input().split())
    s = encrypted_message[start:end]
    print(s)
    encrypted_message = encrypted_message.replace(s, "")
