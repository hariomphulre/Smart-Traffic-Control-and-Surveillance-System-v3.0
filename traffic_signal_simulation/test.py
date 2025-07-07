import lgpio
import time
h = lgpio.gpiochip_open(0)

segments=[2,3,4,14,15,7,8,10]
numbers=[
    [0,0,0,0,0,0,1,0],
    [1,0,0,1,1,1,1,0], 
    [0,0,1,0,0,1,0,0],
    [0,0,0,0,1,1,0,0],  
    [1,0,0,1,1,0,0,0],  
    [0,1,0,0,1,0,0,0],  
    [0,1,0,0,0,0,0,0],   
    [0,0,0,1,1,1,1,0],  
    [0,0,0,0,0,0,0,0], 
    [0,0,0,0,1,0,0,0]   
]
digits=[16,20]

for segment in segments:
    lgpio.gpio_claim_output(h,segment)

lgpio.gpio_claim_output(h,digits[0])
lgpio.gpio_claim_output(h,digits[1])

i=0 
k=5


# ascending
# while True:
#   for n in range (50):
#     for j in range(8):
#       lgpio.gpio_write(h,segments[j], numbers[i][j])
#     lgpio.gpio_write(h,digits[0], 1)
#     lgpio.gpio_write(h,digits[1], 0)
#     time.sleep(0.01)

#     for j in range(8):
#       lgpio.gpio_write(h,segments[j], numbers[k][j])
#     lgpio.gpio_write(h,digits[0], 0)
#     lgpio.gpio_write(h,digits[1], 1)
#     time.sleep(0.01)

#   i+=1
#   if i==10:
#     i = 0
#     k+=1
#     if k==10:
#       k = 0

# decending
while True:
  if i<=3:
    lgpio.gpio_write(h,digits[0],0)
    lgpio.gpio_write(h,digits[1],0)
    time.sleep(0.3)
    lgpio.gpio_write(h,digits[0],1)
    lgpio.gpio_write(h,digits[1],1)

  for n in range (50):
    for j in range(8):
      lgpio.gpio_write(h,segments[j], numbers[i][j])
    lgpio.gpio_write(h,digits[0], 1)
    lgpio.gpio_write(h,digits[1], 0)
    time.sleep(0.01)

    for j in range(8):
      lgpio.gpio_write(h,segments[j], numbers[k][j])
    lgpio.gpio_write(h,digits[0], 0)
    lgpio.gpio_write(h,digits[1], 1)
    time.sleep(0.01)


  i-=1
  if k==0 and i==-1:
    lgpio.gpio_write(h,digits[0],0)
    lgpio.gpio_write(h,digits[1],0)
    break
  if i==-1:
    i = 9
    k-=1
    if k==-1:
      lgpio.gpio_write(h,digits[0],0)
      lgpio.gpio_write(h,digits[1],0)