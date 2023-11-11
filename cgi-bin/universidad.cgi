#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;
my $cgi = CGI->new;
my $nombre = $cgi->param('nombre') || '';
my $licencia = $cgi->param('licencia') || '';
my $departamento = $cgi->param('departamento') || '';
my $denominacion = $cgi->param('denominacion') || '';
print $cgi->header('text/html');
print <<HTML;
<!DOCTYPE HTML>
<html lang="es">
  <head>
    <title>Universidad</title>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="http://localhost/estilosU.css"/>
    <link rel="icon" type="image/png" href="http://localhost/logo1.png"/>
    <meta name="author" content="Victor Gonzalo Maldonado Vilca"/>
  </head>
  <body class="cuerpo">
    <h1 class="titulo"><i>Resultados de B&uacute;squeda<i></h1>
    <div>
      <form method="post" action="http://localhost/Universidad.html">
        <input id="regreso" type="submit" value="Regresar">
      </form>
    </div>
  </body>
</html>
HTML