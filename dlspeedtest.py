import speedtest

speed_test = speedtest.Speedtest()

download_speed = speed_test.download()
download_speed /= (1024*1024)

print(f'Your download speed is {download_speed}')

