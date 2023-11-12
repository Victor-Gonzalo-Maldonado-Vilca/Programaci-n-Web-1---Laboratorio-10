#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;
use Text::CSV;
my $cgi = CGI->new;
my $nombre = $cgi->param('nombre') || '';
my $licencia = $cgi->param('licencia') || '';
my $departamento = $cgi->param('departamento') || '';
my $denominacion = $cgi->param('denominacion') || '';
print $cgi->header(type   => 'text/html',charset => 'utf-8');
my $archivo = '../htdocs/Programas de Universidades.csv';
my $csv = Text::CSV->new({ binary => 1, auto_diag => 1, sep_char => '|' });
open my $ma, '<:encoding(latin1)', $archivo or die "No se puede abrir el archivo CSV: $archivo";
my $header = $csv->getline($ma);
my @resultados;
while(my $fila = $csv->getline($ma)){
  my %datos;
  @datos{@$header} = @$fila;
  if ($datos{'NOMBRE'} =~ /$nombre/i || $datos{'ESTADO_LICENCIAMIENTO'} =~ /$licencia/i ||
    $datos{'DEPARTAMENTO_LOCAL'} =~ /$departamento/i || $datos{'DENOMINACION_PROGRAMA'} =~ /$denominacion/i) {
    push @resultados, \%datos;
  }
}
close $ma;
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
    <h1 class="titulo"><i>Resultados de Búsqueda</i></h1>
    <div>
      <table>
        <tr>
          <th>Nombre de la Universidad</th>
          <th>Estado de licenciamiento</th>
          <th>Departamento Local</th>
          <th>Denominación Programa</th>
        </tr>
      </table>
    </div>
    <div>
      <form method="post" action="http://localhost/Universidad.html">
        <input id="regreso" type="submit" value="Regresar">
      </form>
    </div>
  </body>
</html>
HTML