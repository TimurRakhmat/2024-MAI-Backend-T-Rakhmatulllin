from cache import LRUCache


def main():
    cache = LRUCache(2)
    cache.set('Jesse', 'Pinkman')
    print(cache.cache)
    cache.set('Walter', 'White')
    print(cache.cache)
    cache.set('a', 'a')
    print(cache.cache)
    cache.set('c', 'c')
    print(cache.cache)
    cache.set('b', 'b')
    print(cache.cache)
    
    cache.set('Jesse', 'James')
    print(cache.get('Jesse')) # вернёт 'James'
    #cache.rem('Walter')
    print(cache.get('Walter')) # вернёт ''
    print(cache.cache)

if __name__ == '__main__':
    main()