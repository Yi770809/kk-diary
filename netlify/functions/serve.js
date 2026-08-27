// 素材取图：GET ?key=stickers/xxx.png
const { getStore } = require('@netlify/blobs');

exports.handler = async (event) => {
  try {
    const key = ((event.queryStringParameters || {}).key || '').trim();
    if (!key || !key.startsWith('stickers/')) {
      return { statusCode: 400, body: 'bad key' };
    }
    const store = getStore('kk-stickers');
    const blob = await store.get(key, { type: 'arrayBuffer' });
    if (blob === null) {
      return { statusCode: 404, body: 'not found' };
    }
    const name = key.split('/').pop() || 'img.png';
    const ext = (name.split('.').pop() || 'png').toLowerCase();
    const types = {
      png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg',
      gif: 'image/gif', webp: 'image/webp', svg: 'image/svg+xml',
      bmp: 'image/bmp', ico: 'image/x-icon',
    };
    return {
      statusCode: 200,
      isBase64Encoded: true,
      headers: {
        'Content-Type': types[ext] || 'application/octet-stream',
        'Cache-Control': 'public, max-age=3600',
      },
      body: Buffer.from(blob).toString('base64'),
    };
  } catch (err) {
    return { statusCode: 500, body: String((err && err.message) || err) };
  }
};
