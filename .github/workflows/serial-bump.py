from datetime import datetime
import json
import sys

def bump_serial(now: datetime, serial: int) -> int:
    today = int(now.strftime("%Y%m%d"))
    date = serial // 100
    seq = serial % 100

    if date == today:
        if seq >= 99:
            sys.exit("daily seq number limit reached")
        return serial + 1

    return today * 100 + 1


def format_profile_name(now: datetime, serial: int) -> str:
    seq = serial % 100
    return f"LOVV {now:%d.%m.%Y} #{seq}"


def main():
    now = datetime.now()

    with open("vATIS Profile - LOVV.json", "r+") as file:
        # Load JSON and extract the serial
        data = json.load(file)
        serial = int(data["updateSerial"])

        # Update serial and profile name
        serial = bump_serial(now, serial)
        profile_name = format_profile_name(now, serial)

        data["updateSerial"] = serial
        data["name"] = profile_name

        # Write the changes back to the file
        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()
        
        # Export for use in later steps 
        print(f"serial={serial}")
        print(f"profile_name={profile_name}")

if __name__ == "__main__":
    main()

