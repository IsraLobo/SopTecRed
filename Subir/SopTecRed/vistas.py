from django.http import HttpResponse
from django.shortcuts import render
from SopTecRed import controlInfo
import json

def log(request):
    return render(request, 'loginEdi.html', {'alert':None});


def logout(request):
    try:
        del request.session['user'];
    except KeyError:
        pass
    return render(request, 'loginEdi.html', {'alert':None});


def acceso(request):
    try:
        user = request.POST['username']; cntrs = request.POST['password'];
        try:
            if request.session['user'] == user + cntrs:
                return render(request, 'loginEdi.html',{'alert':'[ERROR]: Este Usuario ya a Iniciado Sesión'});
        except KeyError:
            pass
        nomUser = controlInfo.cosultUser(user,cntrs);
        if nomUser:
            request.session['user'] = user + cntrs;
            return render(request, 'acceso.html',{'user': user, 'nombre': nomUser[0][0]});
        else:
            return render(request, 'loginEdi.html',{'alert':'No existe Información del usuario, [CREDENCIALES INCORRECTAS]'});
    except:
        return render(request, 'loginEdi.html',{'alert':'[ERROR]: Acceso Incorrecto'});
pass


def consulta(request):
    try:
        body_UC = json.loads(request.body.decode('utf-8'));
        msisdn = body_UC['msisdn']; serie = body_UC['serie']; sim = body_UC['sim'];
        resulNum = controlInfo.consultaNum(msisdn,serie,sim);
        return HttpResponse(resulNum);
    except:
        return render(request, 'loginEdi.html',{'alert':'[ERROR]: Acceso Incorrecto'});
pass