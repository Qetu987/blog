from django.shortcuts import render
from records.models import Blog

# Create your views here.

def index(r):
	items = Blog.objects.all()

	def xl(lst, n):
		curent_list = []
		dict_of_ans = {}
		for i in range(n):
			for j in range(i, len(lst), n):
				curent_list.append(lst[j])
			dict_of_ans[i] = curent_list
			curent_list = []
		return dict_of_ans


	xl_list_blog = xl(items, 3)
	md_list_blog = xl(items, 2)

	return render(r, 'index.html', {'items': items, 
									'xl_list_1': xl_list_blog[0], 
									'xl_list_2': xl_list_blog[1], 
									'xl_list_3': xl_list_blog[2], 
									'md_list_1': md_list_blog[0], 
									'md_list_2': md_list_blog[1]})