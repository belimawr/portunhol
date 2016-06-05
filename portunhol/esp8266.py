from portunhol import para_el_portunhol


def web_server():
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Portunhol</title>
            <script src='https://code.jquery.com/jquery-2.2.4.min.js'> </script>
        </head>
        <body>
            <h1>Portugues:</h1>
            <p>%s</p>

            <h1>Portunhol:</h1>
            <p>%s</p>
            
            <div>
                <input type='text' id='palabra'>
                <button id='vai'/>Traduzir</button>
            </div>
            <script>
                $(document).ready(function(){
                    $('#vai').click(function(){
                        var url = 'http://' + window.location.hostname + '/portunhol?palabra=' + encodeURI($('#palabra').val());
                        window.location.href = url;
                    
                    });
                });
            </script>
        </body>
    </html>
    """

    import socket
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    s.settimeout(10)

    print('listening on', addr)
    word = ''
    while True:
        try:
            cl, addr = s.accept()
            print('client connected from', addr)
            cl_file = cl.makefile('rwb', 0)
            read_word = False
            while True:
                line = cl_file.readline()
                line_str = str(line)
                print('Line: ' + line_str)
                if not read_word and line_str.upper().find('GET'):
                    try:
                        word = line_str.split('portunhol?palabra=')[1].split(' ')[0]
                        word = word.replace('%20', ' ')
                        read_word = True
                    except IndexError:
                        pass
                if not line or line == b'\r\n':
                    break
            read_word = False
            translated = para_el_portunhol(word.lower())
            response = html % (word, translated)
            cl.send(response)
            cl.close()
        except Exception:
            try:
                cl.close()
            except Exception:
                pass
        except KeyboardInterrupt:
            print('Good bye!')
            s.close()
            return
