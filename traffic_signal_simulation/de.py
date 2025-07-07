import time
import lgpio

H = lgpio.gpiochip_open(0)
try:
    lgpio.gpio_claim_output(H, 23)
    for _ in range(5):  # Blink 5 times
        lgpio.gpio_write(H, 23, 1)
        time.sleep(0.5)
        lgpio.gpio_write(H, 23, 0)
        time.sleep(0.5)
finally:
    lgpio.gpiochip_close(H)
