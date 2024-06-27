import time
import winsound  # Untuk Windows, gunakan os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq)) untuk Linux

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Waktunya bangun!")
            winsound.Beep(1000, 1000)  # 1000 Hz selama 1000 ms
            break
        time.sleep(30)

set_alarm("06:30")
