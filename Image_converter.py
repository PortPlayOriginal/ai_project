from PIL import Image
def EditImage(Input_Img,side_size,filter_type,zoom_scale):
    #Обрезает края, чтобы получить квадрат
    if Input_Img.width > Input_Img.height:
        Edited_Img = Input_Img.crop(((Input_Img.width-Input_Img.height)/2,0,Input_Img.height+(Input_Img.width-Input_Img.height)/2,Input_Img.height))
    else:
        Edited_Img = Input_Img.crop((0,(Input_Img.height-Input_Img.width)/2,Input_Img.width,Input_Img.width+(Input_Img.height-Input_Img.width)/2))
    #Отрезает с каждой стороны zoom_scale процентов изображения, т.е. zoom_scale = 1 удалит изображение полностью.
    if zoom_scale > 0:
        zoom_scale = min(0.99,zoom_scale)
        Edited_Img = Edited_Img.crop((Edited_Img.width/2*zoom_scale,Edited_Img.height/2*zoom_scale,Edited_Img.width-Edited_Img.width/2*zoom_scale,Edited_Img.height-Edited_Img.height/2*zoom_scale))
    #Изменяет конечный размер изображения
    Edited_Img = Edited_Img.resize((side_size,side_size),resample=0)
    #Редактирует изображение выбранным способом
    Edited_Img = Edited_Img.convert(filter_type)
    return Edited_Img
with Image.open(r"C:\Users\Георгий\Desktop\GFuncs\Input\1.jpg") as IMG:
    IMG = EditImage(IMG,512,"",0)
    IMG.save(r"C:\Users\Георгий\Desktop\GFuncs\Output\final2.png")