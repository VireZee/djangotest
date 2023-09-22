from django.core.management.base import BaseCommand
from app.models import Kategori, Status, Produk
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = ['teknologi', 'psikologi', 'sains']
        for cat in categories:
            Kategori.objects.create(nama_kategori = cat)
            self.stdout.write(self.style.SUCCESS(f'Successfully added Kategori: {cat}'))
        status = ['bisa dijual', 'tidak bisa dijual']
        for stat in status:
            Status.objects.create(nama_status = stat)
            self.stdout.write(self.style.SUCCESS(f'Successfully added Status: {stat}'))
        # cats = Kategori.objects.all()
        # stats = Status.objects.all()
        # for _ in range(10):
        #     product = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(1, 5)))
        #     price = random.randint(1, 50000)
        #     kategori = random.choice(cats)
        #     status = random.choice(stats)
        #     Produk.objects.create(
        #         nama_produk=product,
        #         harga=price,
        #         kategori_id=kategori,
        #         status_id=status
        #     )
        #     self.stdout.write(self.style.SUCCESS(f'Successfully added Produk: {product}, Harga: {price}, Kategori: {kategori.nama_kategori}, Status: {status.nama_status}'))
        books = ['Buku A', 'Buku B', 'Buku C', 'Buku D', 'Buku E']
        categories_index = ['1', '2', '3']
        index = 0
        for book in books:
            kategori = categories_index[index % len(categories_index)]
            kategori = int(kategori)
            kategori_id = Kategori.objects.get(id_kategori=kategori)
            index += 1
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