from django.http import HttpResponse
from django.shortcuts import render, redirect
from importlib_metadata import files
from django.core.files.storage import default_storage
from werkzeug.utils import secure_filename
from classifier.models import Classification

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np 

# Create your views here.
def results(request):
    if request.method == 'POST':
        pass
    else:
        results = Classification.objects.filter().order_by("-id")
        return render(request, "result.html", {'results':results})
def index(request):
    if request.method == 'POST':
        if "file[0]" not in request.FILES:
            print ("no file part")
            return redirect("index")
        
        files_num = len(request.FILES)
        results = []
        for i in range(files_num):
            file_num = "file[" + str(i) + "]"
            file = request.FILES[file_num]
            file_name = default_storage.save(file.name, file)
            result_tuple = (file_name, classify(file_name))
            cl = Classification(image_src = result_tuple[0], result = result_tuple[1])
            cl.save()
            #results += result_tuple
        print ("file(s) was asuccessfully uploaded")
        return HttpResponse("asdfasdf")
        #return render(request, 'result.html', {"results": results})
        #return render(request, 'result.html', {'results': results})
    else:
        return render(request, 'main.html')
    
def classify(filename):
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
    
    img = load_image(filename)
    model = load_model("myModel.h5")
    predict=model.predict(img) 
    class_name=class_names[np.argmax(predict,axis=1)[0]]
    return class_name

def load_image(filename):
	# load the image
	img = load_img("media/" + filename, target_size=(32, 32))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 32, 32, 3)
	# prepare pixel data
	img = img.astype('float32')
	img = img / 255.0
	return img