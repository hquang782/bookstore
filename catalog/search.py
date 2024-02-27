from catalog.models import Product


STRIP_WORDS = ['a','an','and','by','for','from','in','no','not',
 'of','on','or','that','the','to','with'] 

def products(search_text):
    words = _prepare_words(search_text)
    results = {}
    results['products'] = []
    for word in words:
        products = Product.objects.filter(name__icontains=word)
        results['products'] = products
    return results 
def _prepare_words(search_text):
    words = search_text.split()
    for common in STRIP_WORDS:
        if common in words:
            words.remove(common)
    return words[0:5]       