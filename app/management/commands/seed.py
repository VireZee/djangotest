from django.core.management.base import BaseCommand
from app.models import Kategori, Status, Produk
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = ['teknologi', 'psikologi', 'sains']
        status = ['bisa dijual', 'tidak bisa dijual']
        books = ['Buku A', 'Buku B', 'Buku C', 'Buku D', 'Buku E']
        for cat in categories:
            Kategori.objects.create(nama_kategori = cat)
            self.stdout.write(self.style.SUCCESS(f'Successfully added Kategori: {cat}'))
        for stat in status:
            Status.objects.create(nama_status = stat)
            self.stdout.write(self.style.SUCCESS(f'Successfully added Status: {stat}'))
        categories_index = ['1', '2', '3']
        index = 0
        for book in books:
            kategori = categories_index[index % len(categories_index)]
            index += 1
            kategori_id = Kategori.objects.get(id_kategori=kategori)
            if book in ['Buku C', 'Buku D']:
                status_id = Status.objects.get(id_status=2)
            else:
                status_id = Status.objects.get(id_status=1)
            Produk.objects.create(
                nama_produk = book,
                harga = random.randint(1, 50000),
                kategori_id = kategori_id,
                status_id = status_id
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully added Produk: {book}'))