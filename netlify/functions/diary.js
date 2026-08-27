// 手账数据：GET 读取 / POST 保存（存 Netlify Blobs）
const { getStore } = require('@netlify/blobs');

exports.handler = async (event) => {
  try {
    const store = getStore('kk-stickers');
    const KEY = 'diary/pages.json';

    if (event.httpMethod === 'GET') {
      const blob = await store.get(KEY);
      const body = blob ? Buffer.from(blob).toString('utf-8') : '{"pages":{}}';
      return {
        statusCode: 200,
        headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', 'Access-Control-Allow-Origin': '*' },
        body,
      };
    }

    if (event.httpMethod === 'POST') {
      const raw = JSON.parse(event.body || '{}');
      if (!raw || typeof raw.pages !== 'object') {
        return { statusCode: 400, body: JSON.stringify({ error: '需要 pages 字段' }) };
      }
      await store.set(KEY, JSON.stringify(raw), {
        metadata: { updatedAt: new Date().toISOString(), type: 'diary' },
      });
      return { statusCode: 200, body: JSON.stringify({ ok: true }) };
    }

    return { statusCode: 405, body: JSON.stringify({ error: 'method not allowed' }) };
  } catch (err) {
    return { statusCode: 500, body: JSON.stringify({ error: String((err && err.message) || err) }) };
  }
};
