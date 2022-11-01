from django.shortcuts import render, redirect
from faperta.models import Dosen, Staf, Mahasiswa
from faperta.forms import FormDosen, FormStaf, FormMahasiswa
from django.contrib import messages


# Create your views here.
def hapus_Dosen(request, id_Dosen):
    Dosen = Dosen.objects.filter(id=id_Dosen)
    Dosen.delete()

    messages.success(request, "Data Berhasil Dihapus!")
    return redirect('Dosen')

def ubah_Dosen(request, id_Dosen):
    Dosen = Dosen.objects.get(id=id_Dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui!")
            return redirect('ubah_Dosen', id_Dosen=id_Dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form':form,
            'dosen':dosen,
        }    

    return render(request, template, konteks)    

def indexfaperta(request):
    return render(request, 'faperta.html')


def tambah_Dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form =FormDosen()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)

    else:
        form = FormDosen()
   
    konteks = {
        'form': form,
    }

    return render(request, 'tambah-dosen.html', konteks)

def tambah_staf(request):
     if request.POST:
        form = FormStaf(request.POST)
        if form.is_valid():
            form.save()
            form =FormStaf()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-staf.html', konteks)

        else:
         form = FormStaf()

        konteks = {
        'form': form,
         }

        return render(request, 'tambah-staf.html', konteks)

def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form' : form,
                'pesan': pesan,
            }

            return render (request, 'tambah-mahasiswa.html', konteks)
    else: 
        form = FormMahasiswa()

    konteks = {
        'form': form
    }

    return render(request, 'tambah-mahasiswa.html', konteks)