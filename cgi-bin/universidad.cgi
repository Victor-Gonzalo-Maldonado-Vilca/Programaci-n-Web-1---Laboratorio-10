#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;
use Text::CSV;
my $cgi = CGI->new;
$cgi->charset('latin-1');
my $nombre = uc($cgi->param('nombre')) || '';
my $licencia = uc($cgi->param('licencia')) || '';
my $departamento = uc($cgi->param('departamento')) || '';
my $denominacion = uc($cgi->param('denominacion')) || '';
print $cgi->header(type   => 'text/html',charset => 'latin-1');
my $archivo = '../htdocs/Programas de Universidades.csv';
my $csv = Text::CSV->new({ binary => 1, auto_diag => 1, sep_char => '|' });
open my $ma, '<:encoding(latin-1)', $archivo or die "No se puede abrir el archivo CSV: $archivo";
my $header = $csv->getline($ma);
my @resultados;
while(my $fila = $csv->getline($ma)){
  my %datos;
  @datos{@$header} = @$fila;
  if ($datos{'NOMBRE'} eq $nombre || $datos{'PERIODO_LICENCIAMIENTO'} eq $licencia ||
    $datos{'DEPARTAMENTO_LOCAL'} eq $departamento || $datos{'DENOMINACION_PROGRAMA'} eq $denominacion) {
    push @resultados, \%datos;
  }
}
close $ma;
print <<HTML;
<!DOCTYPE HTML>
<html lang="es">
  <head>
    <title>Universidad</title>
    <meta charset="latin-1"/>
    <link rel="stylesheet" href="http://localhost/estilosU.css"/>
    <link rel="icon" type="image/png" href="http://localhost/logo1.png"/>
    <meta name="author" content="Victor Gonzalo Maldonado Vilca"/>
  </head>
  <body class="cuerpo">
    <h1 class="titulo"><i>Resultados de la Consulta</i></h1>
    <div>
      <table id="tabla" border="1">
        <tr>
          <th>Nombre Universidad</th>
          <th>Per&iacute;odo de licenciamiento</th>
          <th>Departamento Local</th>
          <th>Denominaci&oacute;n Programa</th>
        </tr>
HTML
foreach my $resultado(@resultados){
  print "<tr id='otrasfila'>";
  print "<td class='columna'>$resultado->{'NOMBRE'}</td>";
  print "<td class='columna'>$resultado->{'PERIODO_LICENCIAMIENTO'}</td>";
  print "<td class='columna'>$resultado->{'DEPARTAMENTO_LOCAL'}</td>";
  print "<td class='ultimac'>$resultado->{'DENOMINACION_PROGRAMA'}</td>";
  print "</tr>";
}
print <<HTML;
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