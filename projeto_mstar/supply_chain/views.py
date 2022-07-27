from re import M
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import LocalForm, MercadoriaForm, EntradaForm, SaidaForm
from .models import Mercadoria, Local, Entrada, Saida

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



def index(request):
    mercadorias = Mercadoria.objects.all()
    locais = Local.objects.all()
    entradas = Entrada.objects.all()
    saidas = Saida.objects.all()
    datas_entradas = []
    quantidade_entradas = []
    datas_saidas = []
    quantidade_saidas = []

    dados_entradas = Entrada.objects.order_by('data')
    for dado_entrada in dados_entradas:
        datas_entradas.append(dado_entrada.data.strftime("%d/%m/%Y"))
        quantidade_entradas.append(dado_entrada.quantidade)
    

    dados_saidas = Saida.objects.order_by('data')
    for dado_saida in dados_saidas:
        datas_saidas.append(dado_saida.data.strftime("%d/%m/%Y"))
        quantidade_saidas.append(dado_saida.quantidade)
    

    
    return render(request, 'supply_chain/index.html',{
    'mercadorias': mercadorias,
    'locais': locais,
    'entradas': entradas,
    'saidas': saidas,
    'datas_entradas': datas_entradas,
    'quantidades_entradas':quantidade_entradas,
    'datas_saidas': datas_saidas,
    'quantidades_saidas':quantidade_saidas})


def gerar_pdf(request):
    template_path = 'supply_chain/pdf.html'
    entradas = Entrada.objects.all().order_by('data')
    saidas = Saida.objects.all().order_by('data')
    for entrada in entradas:
        entrada.data = entrada.data.strftime("%d/%m/%Y")
    for saida in saidas:
        saida.data = saida.data.strftime("%d/%m/%Y")
    context = {
    'entradas': entradas,
    'saidas': saidas}
   
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'
    
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def relatorio_mercadoria(request, id):
    datas_entradas = []
    quantidade_entradas = []
    datas_saidas = []
    quantidade_saidas = []

    meses_entradas = {'Janeiro':[],
            'Fevereiro':[],
            'Março':[],
            'Abril':[],
            'Maio':[],
            'Junho':[],
            'Julho':[],
            'Agosto':[],
            'Setembro':[],
            'Outubro':[],
            'Novembro':[],
            'Dezembro':[]}
    meses_saidas = {'Janeiro':[],
            'Fevereiro':[],
            'Março':[],
            'Abril':[],
            'Maio':[],
            'Junho':[],
            'Julho':[],
            'Agosto':[],
            'Setembro':[],
            'Outubro':[],
            'Novembro':[],
            'Dezembro':[]}

    i = 1
    dados_entradas = Entrada.objects.filter(mercadoria=id).order_by('data')
    for mes in meses_entradas.keys():
        for dado_entrada in dados_entradas:
            if dado_entrada.data.month == i:
                meses_entradas[mes].append(dado_entrada.quantidade)
        if meses_entradas[mes]:
            meses_entradas[mes] = sum(meses_entradas[mes])
        i+=1
            
    for mes, quantidade in meses_entradas.items():
        if meses_entradas[mes]:
            datas_entradas.append(mes)
            quantidade_entradas.append(quantidade)

    
    i = 1
    dados_saidas = Saida.objects.filter(mercadoria=id).order_by('data')
    for mes in meses_saidas.keys():
        for dado_saida in dados_saidas:
            if dado_saida.data.month == i:
                meses_saidas[mes].append(dado_saida.quantidade)
        if meses_saidas[mes]:
            meses_saidas[mes] = sum(meses_saidas[mes])
        i+=1
            
    for mes, quantidade in meses_saidas.items():
        if meses_saidas[mes]:
            datas_saidas.append(mes)
            quantidade_saidas.append(quantidade)
    

    return render(request, 'supply_chain/relatorio_mercadoria.html',{
        'datas_entradas': datas_entradas,
        'quantidades_entradas':quantidade_entradas,
        'datas_saidas': datas_saidas,
        'quantidades_saidas':quantidade_saidas
    })

def cadastro_local(request):
    if request.method == 'GET':
        local_form = LocalForm()
    else:
        local_form = LocalForm(request.POST)
        if local_form.is_valid():
            local_form.save()
            return redirect(reverse('index'))
    return render(request, 'supply_chain/cadastro_local.html', {
            'form': local_form,  
        })
        

def cadastro_mercadoria(request):
    if request.method == 'GET':  
        mercadoria_form = MercadoriaForm()
    else:
        mercadoria_form = MercadoriaForm(request.POST)
        if mercadoria_form.is_valid():
            mercadoria_form.save()
            return redirect(reverse('index'))
    return render(request, 'supply_chain/cadastro_mercadoria.html', {
        'form': mercadoria_form,  
    })


def cadastro_entrada(request):
    if request.method == 'GET':    
        entrada_form = EntradaForm()
    else:
        entrada_form = EntradaForm(request.POST)
        if entrada_form.is_valid():
            entrada_form.save()
            return redirect(reverse('index'))
    return render(request, 'supply_chain/cadastro_entrada.html', {
        'form': entrada_form,  
    })


def cadastro_saida(request):
    if request.method == 'GET':    
        saida_form = SaidaForm()
    else:
        saida_form = SaidaForm(request.POST)
        if saida_form.is_valid():
            saida_form.save()
            return redirect(reverse('index'))
    return render(request, 'supply_chain/cadastro_saida.html', {
        'form': saida_form,  
    })

def delete_local(request, id):
    local_deletado = Local.objects.get(id=id)
    local_deletado.delete()
    return redirect(reverse('index'))


def delete_mercadoria(request, id):
    mercadoria_deletada = Mercadoria.objects.get(id=id)
    mercadoria_deletada.delete()
    return redirect(reverse('index'))


def delete_entrada(request, id):
    entrada_deletada = Entrada.objects.get(id=id)
    entrada_deletada.delete()
    return redirect(reverse('index'))


def delete_saida(request, id):
    saida_deletada = Saida.objects.get(id=id)
    saida_deletada.delete()
    return redirect(reverse('index'))


def edita_local(request, id):
    local_existente = Local.objects.get(pk=id)
    if request.method == 'GET':
        local_form = LocalForm(instance=local_existente)
    else:
        local_form = LocalForm(request.POST, instance=local_existente)
        if local_form.is_valid():
            local_form.save()
            return redirect(reverse('index'))
    return render(request, 'supply_chain/cadastro_local.html', {
            'form': local_form,  
        })

def edita_mercadoria(request, id):
    mercadoria_existente = Mercadoria.objects.get(id=id)
    if request.method == 'GET':
        mercadoria_form = MercadoriaForm(instance=mercadoria_existente)
    else:
        mercadoria_form = MercadoriaForm(request.POST, instance=mercadoria_existente)
        if mercadoria_form.is_valid():
            mercadoria_form.save()
            return redirect(reverse('index'))
    return render(request, 'supply_chain/cadastro_mercadoria.html', {
            'form': mercadoria_form,  
        })

def edita_entrada(request, id):
    entrada_existente = Entrada.objects.get(pk=id)
    if request.method == 'GET':
        entrada_form = EntradaForm(instance=entrada_existente)
    else:
        entrada_form = EntradaForm(request.POST, instance=entrada_existente)
        if entrada_form.is_valid():
            entrada_form.save()
            return redirect(reverse('index'))
    return render(request, 'supply_chain/cadastro_entrada.html', {
            'form': entrada_form,  
        })

def edita_saida(request, id):
    saida_existente = Saida.objects.get(pk=id)
    if request.method == 'GET':
        saida_form = SaidaForm(instance=saida_existente)
    else:
        saida_form = SaidaForm(request.POST, instance=saida_existente)
        if saida_form.is_valid():
            saida_form.save()
            return redirect(reverse('index'))
    return render(request, 'supply_chain/cadastro_saida.html', {
            'form': saida_form,  
        })