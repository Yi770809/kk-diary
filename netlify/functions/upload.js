// 素材上传：POST JSON {name, category, data(base64), type}
const { getStore } = require('@netlify/blobs');

const ALLOWED_CATS = ['花草', '星星月亮', '天空', '爱心', '小动物', '表情包照片', '其他'];

exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }
  try {
    const body = JSON.parse(event.body || '{}');
    let name = String(body.name || '').trim();
    let title = String(body.title || '').trim().slice(0, 30);
    let category = String(body.category || '其他').trim();
    const data = body.data || '';
    const type = String(body.type || 'image/png');

    if (!name || !data) {
      return { statusCode: 400, body: JSON.stringify({ ok: false, error: '缺少文件名或内容' }) };
    }
    if (!ALLOWED_CATS.includes(category)) category = '其他';

    // 清理文件名（防路径穿越）
    name = name.replace(/[^\w.\u4e00-\u9fa5-]+/g, '_').slice(0, 60);
    const key = `stickers/${category}/${Date.now()}_${name}`;
    const store = getStore('kk-stickers');
    await store.set(key, Buffer.from(data, 'base64'), {
      metadata: { name, category, type, title },
    });
    return { statusCode: 200, body: JSON.stringify({ ok: true, key }) };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ ok: false, error: String((err && err.message) || err) }),
    };
  }
};
