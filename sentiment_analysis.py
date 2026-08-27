# مشروع تحليل مشاعر النصوص العربية باستخدام بايثون
# مخصص لمعرض أعمال المطور: محمد السيروان

def analyze_arabic_sentiment(text):
    # قوائم الكلمات المفتاحية المخصصة للتصنيف
    positive_words = ["ممتاز", "رائع", "جميل", "ناجح", "مبهر", "شكرا", "كفو", "ذكي", "سعيد"]
    negative_words = ["سيء", "فاشل", "صعب", "مخيب", "حزين", "رفض", "خطأ", "ضعيف", "مشكلة"]
    
    # تحويل النص إلى كلمات منفصلة
    words = text.split()
    
    positive_score = 0
    negative_score = 0
    
    # فحص الكلمات وحساب النقاط
    for word in words:
        if word in positive_words:
            positive_score += 1
        elif word in negative_words:
            negative_score += 1
            
    # تحديد النتيجة النهائية بناءً على المقارنة
    if positive_score > negative_score:
        return "إيجابي (Positive) 😊"
    elif negative_score > positive_score:
        return "سلبي (Negative) 😔"
    else:
        return "محايد (Neutral) 😐"

# تجربة النموذج البرمجي ببيانات مختلفة
if __name__ == "__main__":
    print("--- تشغيل نموذج الذكاء الاصطناعي لتحليل المشاعر ---")
    
    test_1 = "هذا المشروع رائع جدا ومبهر للشركات"
    test_2 = "واجهت مشكلة صعبة والبرنامج سيء جدا"
    test_3 = "الكود مكتوب بلغة بايثون اليوم"
    
    print(f"النص: '{test_1}' -> النتيجة: {analyze_arabic_sentiment(test_1)}")
    print(f"النص: '{test_2}' -> النتيجة: {analyze_arabic_sentiment(test_2)}")
    print(f"النص: '{test_3}' -> النتيجة: {analyze_arabic_sentiment(test_3)}")
