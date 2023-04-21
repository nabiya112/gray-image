from PIL import Image

# 이미지 열기 경로는 자신의 이미지가 저장된 폴더로 
image = Image.open('D:\\cam\\hamo01.png')

# 이미지 좌우 반전하기
flipped_image = image.transpose(method=Image.FLIP_LEFT_RIGHT)

# 이미지 그레이스케일로 변환하기
gray_image = flipped_image.convert('L')

# 변환된 이미지 저장하기
gray_image.save('gray_flipped_image.jpg')

# 변환된 이미지 창에 띄우기
gray_image.show()

