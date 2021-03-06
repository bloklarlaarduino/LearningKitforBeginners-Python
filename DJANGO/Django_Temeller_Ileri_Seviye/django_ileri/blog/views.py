from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import Blog
from .forms import IletisimForm, BlogForm
from django.contrib import messages
from django.http import JsonResponse


def deneme(request):
    if request.is_ajax():  # ajax istekler için bu şekilde kullanmalıyız. eğer method ajax ise
        print("istek geldi")
        return True
    return render(request, 'deneme.html')


def iletisim(request):
    form = IletisimForm(
        data=request.GET or None)  # formumuzdan bir instance oluşturuyoruz, data= -> eğer varsa GET'ten gelenleri al inputlara yerleştir yoksa boş geç
    # print(request.GET.get('email')) # GET içerisindeki değerleri yakalarız
    if form.is_valid():  # eğer formdan gelen bilgiler doğru ise
        isim = form.cleaned_data.get('isim')  # form içindeki bilgileri yakalayabiliyoruz
        soyisim = form.cleaned_data.get('soyisim')
        email = form.cleaned_data.get('email')
        icerik = form.cleaned_data.get('icerik')
        print(icerik, email, isim, soyisim)
    return render(request, 'blog/iletisim.html', {'form': form})  # formu contexte gönderiyoruz


def posts_list(request):
    posts = Blog.objects.all()
    if (request.GET.get('deneme')):
        get = request.GET.get('deneme')
        return render(request,
                      "blog/posts_list.html", context={
                'posts': posts, 'get': get})
    return render(request,
                  "blog/posts_list.html", context={
            'posts': posts})  # ilk önce zorunlu olarak request'i göndermeliyiz, daha sonra template'i daha sonra contexti. context bir sözlüktür


def post_update(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    isim = post.title
    form = BlogForm(request.POST or None,
                    instance=post,
                    files=request.FILES or None)  # instance -> formun datasını verdiğimiz instance ile dolduruyoruz
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        slug = post.slug  # başlık güncellenirse yeni slug'ı seçiyoruz
        messages.success(request, "{} başlıklı post başarıyla güncellendi".format(isim), extra_tags="success")
        return redirect(reverse('blog:post_detail', kwargs={'slug': slug}))
    return render(request, 'blog/post_update.html', context={'form': form, 'post': post})


def post_delete(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    post.delete()
    messages.success(request, "{} başlıklı makale başarıyla silindi".format(post.title), extra_tags="warning")
    return redirect(reverse("blog:posts_list"))


def post_create(request):
    form = BlogForm()
    if request.method == "POST":  # eğer method POST ise
        form = BlogForm(data=request.POST,
                        files=request.FILES or None)  # yeni bir form oluştur ve oluşturduğun formun içine bu datayı yaz
        if form.is_valid():
            created_blog = form.save(
                commit=False)  # commit False olunca oluşacak nesneyi döndürür fakat veritabanına henüz ekleme yapmaz

            created_blog.save()  # commit False yaptığımız için oluşturduğumuz instance'i tekrardan kayıt ediyoruz
            messages.success(request, "{} başlıklı post başarıyla oluşturuldu".format(created_blog.title),
                             extra_tags="success")
            # request'e mesaj yolladık. extra_tags diyerek class vermeyi sağladık
            return redirect(reverse("blog:post_detail",
                                    kwargs={'slug': created_blog.slug}))  # bu sayede parametreli redirect yapabiliriz

    return render(request, 'blog/post_create.html', context={'form': form})


def post_detail(request, slug):  # bir id parametresi alacak dedik
    # blog = Blog.objects.get(pk=id)
    blog = get_object_or_404(Blog,
                             slug=slug)  # eğer bulamazsa 404 döndürür. ilk parametre modelimiz ikinci parametre filtremiz
    return render(request, 'blog/post_detail.html', context={'post': blog})
