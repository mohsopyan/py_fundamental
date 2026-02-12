transaksi = {
    "pembeli": "Moyan",
    "total_belanja": 150000,
    "member": True
}

def cek_promo(discount):
    if discount["total_belanja"] > 200000 and discount["member"]:
        return "Dapat Diskon 20%"
    else:
        return "Harga Normal"
    
status_promo = cek_promo(transaksi)
print(f"Halo {transaksi['pembeli']}, lakukan pembayaran dengan {status_promo}")