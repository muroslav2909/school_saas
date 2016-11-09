workfile = '/home/myroslav/virtual_env_project/school_saas/school_saas/saas/static/img/school_images/2.txt'
f = open(workfile, 'r')
raw = f.read()
img2 = Image.frombytes('RGB', (100, 100), raw)
img2.save('/home/myroslav/virtual_env_project/school_saas/school_saas/saas/static/img/school_images/sssqqq.jpg')


workfile = '/home/myroslav/virtual_env_project/school_saas/school_saas/saas/static/img/school_images/2.txt'
f = open(workfile, 'r')
raw = f.read()
import base64
encoded = raw.decode('base64')
img2 = Image.frombytes('RGB', (90, 90), encoded)
img2.save('/home/myroslav/virtual_env_project/school_saas/school_saas/saas/static/img/school_images/sssqqq.jpg')




img = Image.open("/home/myroslav/virtual_env_project/school_saas/school_saas/static/img/school_images/p3.jpg")
raw = img.tobytes()
img2 = Image.frombytes(img.mode, img.size, raw)
img2.save('/home/myroslav/virtual_env_project/school_saas/school_saas/static/img/school_images/11111.jpg')
