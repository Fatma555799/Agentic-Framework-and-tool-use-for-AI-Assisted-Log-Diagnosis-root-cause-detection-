from pymavlink import mavutil
import sys

if len(sys.argv) < 2:
    print("Usage: python inspect_log.py your_log.bin")
    sys.exit(1)

log_path = sys.argv[1]
mlog = mavutil.mavlink_connection(log_path)

print("messages in the log: ")
message_types = set()

while True:
    msg = mlog.recv_match(blocking=False)
    if msg is None:
        break
    msg_type = msg.get_type()
    message_types.add(msg_type)
    
    # print the first 5 messages of each type so we don't print too much
    if list(message_types).count(msg_type) <= 5:
        print(f"\n--- {msg_type} ---")
        print(msg.to_dict())

print("\nAll message types present in the log:")
print(sorted(message_types))