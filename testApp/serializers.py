from rest_framework import serializers
from .models import Post

# Postモデルの翻訳用シリアライザ (JSON変換を担当)
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # 翻訳対象のモデル
        fields = ['id', 'content', 'created_at']  # JSONに含めるフィールド
