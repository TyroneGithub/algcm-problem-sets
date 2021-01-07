def partition(movies, l, r):
  pivot = movies[r]
  dump = l

  for trash_col in range(l, r):
    if movies[trash_col] <= pivot:
      movies[trash_col], movies[dump] = movies[dump], movies[trash_col]
      dump += 1

  movies[r], movies[dump] = movies[dump], movies[r]
  
  return dump

def quick_sort(movies, key, l, r):

  if key >= 0 and key <= r - l  +1:
    p = partition(movies, l, r)
    if p - l == key:
      return movies[p]
    if p - l > key:
      return quick_sort(movies, key, l, p - 1)
    return quick_sort(movies, key - p + l - 1 , p + 1, r)
  
  return 0
      # return quick_sort(movies, key, p, r)


def last_watched(movies, num_movies):
    if num_movies == 0:
        last_watched = -1
    elif num_movies >= len(movies):
        last_watched = quick_sort(movies, 0, 0, len(movies) - 1)
        # print(last_watched)
    else:
        last_watched = quick_sort(movies,len(movies) - num_movies, 0, len(movies) - 1)
    
    print(last_watched)



n = int(input())
movies = []
# movies = [2, 4, 5, 9, 1, 3, 12, 17] 
# [1, 2, 3, 4, 5, 9, 12, 17]
for i in range(n):
    r,c = list(map(int,input().rstrip().split(" ")))
    movies.append(r-c)
# s, e, a, k = [0, 7, 5, 1]
q = int(input())
for cc in range(q):
    s,e,a,k = list(map(int,input().rstrip().split(" ")))
    last_watched(movies[s:e+1], a//k)
# print(len)
    # solve for answer here
