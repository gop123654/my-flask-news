from flask import Flask, render_template

app = Flask(__name__)

# -------------------------------
# 🔹 ข้อมูลจำลอง (ข่าวทั้งหมด)
# -------------------------------
articles = [
    {
        "id": 1,
        "title": "โปรเจกต์ Flask สุดเจ๋ง!",
        "category": "โปรเจกต์",
        "image": "images/news1.jpg",
        "summary": "เว็บนี้สร้างด้วย Flask และ Bootstrap ภายในเวลาไม่ถึงวัน",
        "content": """
        <p>นี่คือรายละเอียดของโปรเจกต์ Flask ที่คุณสร้างขึ้นเอง...</p>

<img src="/static/images/content1-1.jpg" 
     class="img-fluid rounded my-3 w-50 mx-auto d-block" 
     alt="ตัวอย่างโค้ด">
<p class="text-muted text-center"><small>รูปที่ 1: ตัวอย่างโค้ด Flask</small></p>

<p>การพัฒนาเว็บแอปพลิเคชันด้วย Flask นั้นง่ายและรวดเร็ว...</p>

<img src="/static/images/content1-2.jpg" 
     class="img-fluid rounded my-3 w-75" 
     alt="ผลลัพธ์">
<p class="text-muted text-center"><small>รูปที่ 2: ผลลัพธ์ที่ได้</small></p>
"""
    },
    {
        "id": 2,
        "title": "เรียนรู้ Python ง่ายกว่าที่คิด",
        "category": "เทคโนโลยี", 
        "image": "images/news2.jpg",
        "summary": "เริ่มจาก 0 ก็สร้างเว็บได้จริง",
        "content": """
        <p>Python เป็นภาษาที่เหมาะกับผู้เริ่มต้นและมีชุมชนใหญ่...</p>
        
        <img src="{{ url_for('static', filename='images/content2-1.jpg') }}" 
             class="img-fluid rounded my-3" alt="โครงสร้าง Python">
        <p class="text-muted text-center"><small>รูปที่ 1: โครงสร้างภาษา Python</small></p>
        
        <p>สามารถใช้พัฒนาได้ทั้งเว็บแอปฯ, Data Science, AI และอื่นๆ...</p>
        """
    },
    {
        "id": 3,
        "title": "Portfolio ของฉัน",
        "category": "ผลงาน",
        "image": "images/Portfolio.jpg",
        "summary": "รวมผลงานด้านโปรแกรมมิ่งและเว็บดีไซน์ไว้ที่นี่",
        "content": """
        <div class="row my-4">
    <!-- รูปที่ 1 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-1.jpg" 
             class="img-fluid rounded shadow" >
    </div>
    <!-- รูปที่ 2 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-2.jpg" 
             class="img-fluid rounded shadow" >
    </div>
</div> 
<div class="row my-4">
<!-- รูปที่ 1 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-3.jpg" 
             class="img-fluid rounded shadow" >
    </div>
    <!-- รูปที่ 2 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-4.jpg" 
             class="img-fluid rounded shadow" >
    </div>
</div> 
<div class="row my-4">
<!-- รูปที่ 1 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-5.jpg" 
             class="img-fluid rounded shadow" >
    </div>
    <!-- รูปที่ 2 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-6.jpg" 
             class="img-fluid rounded shadow" >
    </div>
</div> 
<div class="row my-4">
<!-- รูปที่ 1 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-7.jpg" 
             class="img-fluid rounded shadow" >
    </div>
    <!-- รูปที่ 2 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-8.jpg" 
             class="img-fluid rounded shadow" >
    </div>
</div> 
<div class="row my-4">
<!-- รูปที่ 1 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-9.jpg" 
             class="img-fluid rounded shadow" >
    </div>
    <!-- รูปที่ 2 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-10.jpg" 
             class="img-fluid rounded shadow" >
    </div>
</div> 
<div class="row my-4">
<!-- รูปที่ 1 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-11.jpg" 
             class="img-fluid rounded shadow" >
    </div>
    <!-- รูปที่ 2 -->
    <div class="col-md-6 text-center">
        <img src="/static/images/content3-12.jpg" 
             class="img-fluid rounded shadow" >
    </div>
</div> 

"""
    },
    {
        "id": 4,
        "title": "20018/ทีม Londo Bell/โรงเรียนวิสุทธิกษัตรี",
        "category": "ผลงาน",
        "image": "images/news4.jpg",
        "summary": "คลิปวิดีโอสั้น ในหัวข้อ 'เปิดใจก่อนเปิดจอ'",
        "content":"""
        <div class="row my-4 ">
        <div class="col-md-4 text-center">
        <img src="/static/images/content4-1.jpg" 
             class="img-fluid rounded shadow" >
        </div>

        <div class="col-md-4 text-center">
        <img src="/static/images/content4-2.jpg" 
             class="img-fluid rounded shadow" >
        </div>
        <div class="col-md-4 text-center">
        <img src="/static/images/content4-3.jpg" 
             class="img-fluid rounded shadow" >
        </div>
       
                <a href="https://youtu.be/E60QZ7RQEiQ?si=Ydho5BDpLsN5IPCU" target="_blank" class="text-decoration-none">
                    <div class="p-3 border rounded h-100">
                        <div class="text-danger mb-2">▶</div>
                        <h6>20018/ทีม Londo Bell/โรงเรียนวิสุทธิกษัตรี</h6>
                    </div>
                </a>
                
        </div>"""
    },
    {
        "id": 5,
        "title": "BRAND’S ProXperience job shadow",
        "category": "ผลงาน",
        "image": "images/news5.jpg",
        "summary": "ประสบการฝึกงานโปรแกรมเมอ และฝึกการทำ Frontend Backend",
        "content": """
        <p>ผมได้ถูกคัดเลือกจากคน 1000 ในกิจกรรม BRAND’S ProXperience โดยได้ไปฝึกงานในธานะ โปรแกรมเมอร์</p>
        
        <img src="/static/images/content5-1.jpg" 
     class="img-fluid rounded my-3 w-50 mx-auto d-block" >
        
        """
    },
    {
        "id": 6,
        "title": "สูตรรัก รสเดช",
        "category": "เทคโนโลยี",
        "image": "images/news6.jpg",
        "summary": "เรียนรู้การจัดการเวอร์ชันโค้ดอย่างมืออาชีพ",
        "content": """
        <p>Git และ GitHub เป็นเครื่องมือสำคัญสำหรับนักพัฒนาซอฟต์แวร์...</p>
        
        <img src="{{ url_for('static', filename='images/content6-1.jpg') }}" 
             class="img-fluid rounded my-3" alt="Git Workflow">
        <p class="text-muted text-center"><small>รูปที่ 1: Git Workflow</small></p>
        
        <p>การใช้ Git อย่างถูกวิธีช่วยให้การทำงานร่วมกับทีมเป็นไปอย่างราบรื่น...</p>
        """
    }
]

# -------------------------------
# 🔹 ฟังก์ชันช่วยแยกหมวด
# -------------------------------
def get_categories():
    return sorted(list(set([a['category'] for a in articles])))

# -------------------------------
# 🔹 หน้า Home
# -------------------------------
@app.route('/')
def home():
    categories = get_categories()
    return render_template('index.html', articles=articles, categories=categories)

# -------------------------------
# 🔹 หน้าแสดงข่าวตามหมวด
# -------------------------------
@app.route('/category/<string:name>')
def category(name):
    filtered = [a for a in articles if a["category"] == name]
    categories = get_categories()
    return render_template('category.html', articles=filtered, category_name=name, categories=categories)

# -------------------------------
# 🔹 หน้าแสดงเนื้อหาข่าว
# -------------------------------
@app.route('/article/<int:id>')
def article(id):
    item = next((a for a in articles if a["id"] == id), None)
    categories = get_categories()
    return render_template('article.html', article=item, categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
