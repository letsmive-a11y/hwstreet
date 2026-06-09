from PIL import Image, ImageDraw

def generate_caption(nama, merk, kondisi, harga, tanggal):
    tanggal_str = tanggal.strftime('%d %B %Y %H:%M')
    return f"""
🔥 LELANG DIECAST 🔥

🚗 {nama}
🏷️ Merk: {merk}
📦 Kondisi: {kondisi}
💰 Open Bid: Rp {harga}

⏰ Tanggal: {tanggal_str}

Langsung gas sebelum kehabisan!
#hotwheels #diecast #lelang
"""