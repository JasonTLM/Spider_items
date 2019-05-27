# coding=utf-8
from lxml import etree

text = """
<table>
<tbody>
<tr class="zonedword-switch setting-checked">
<td><span class="check-label">划词翻译</span></td>
<td><span class="check-option"></span></td>
</tr>
<tr class="realtrans-switch setting-checked">
<td><span class="check-label">实时翻译</span></td>
<td><span class="check-option"></span></td>
</tr>
<tr class="history-switch setting-checked">
<td><span class="check-label">历史记录</span></td>
<td><span class="check-option"></span></td>
</tr>
<tr>
<td colspan="2"><hr class="split-line"/></td>
</tr>
<tr class="sound-spd-switch">
<td><span class="check-label">发音语速</span></td>
<td><div class="sound-spd-items"><span id="spd-slow" class="sound-spd-radio" data-value="slow"><span class="icon-radio radio-btn"></span>较慢</span><span id="spd-normal" class="sound-spd-radio" data-value="normal" checked><span class="icon-radio radio-btn"></span>中速</span><span id="spd-fast" class="sound-spd-radio" data-value="fast"><span class="icon-radio radio-btn"></span>较快</span></div></td>
</tr>
<tr class="sound-prefer-switch">
<td><span class="check-label">英语发音偏好</span></td>
<td><div class="sound-prefer-items"><span id="prefer-en" class="sound-prefer-radio" data-value="en" checked><span class="icon-radio radio-btn"></span>美式</span><span id="prefer-uk" class="sound-prefer-radio" data-value="uk"><span class="icon-radio radio-btn"></span>英式</span></div></td>
</tr>
<tr class="sound-trigger-switch">
<td><span class="check-label">发音模式</span></td>
<td><div class="sound-trigger-items"><span id="click-trigger" class="sound-trigger-radio" data-value="click"><span class="icon-radio radio-btn"></span>点击发音</span><span id="hover-trigger" class="sound-trigger-radio" data-value="hover" checked><span class="icon-radio radio-btn"></span>自动发音</span></div></td>
</tr>
</tbody>
</table>"""

def html_Text():
    parser = etree.HTMLParser(encoding='utf-8')
    html_file_text = etree.HTML('boss.html',parser=parser)
    # # print(html_file_text)
    # html_file_text = etree.HTML(text)
    print(etree.tostring(html_file_text,encoding='utf-8').decode('utf-8'))

def parse_file():
    parse = etree.HTMLParser(encoding='utf-8')
    html_file = etree.parse(text,parser=parse)
    print(etree.tostring(html_file,encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    parse_file()
    # html_Text()
