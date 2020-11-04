% Emilio Bernal, Ian Odria, Erasmo Villarreal, Gabriela Gallardo, Jose Romo

clear;
clf;

% Inicializar variables
height = input("Cual es la altura del volcan?\n");
diameter = input("Cual es el diametro del volcan?\n");
n = input("Cuantas trayectorias quieres simular?\n");
g = -9.8;
% Donde guardo la matriz de la trayectoria
tabla = cell(1,n);
dt = 0.2;
color = zeros(n,3);

% Genera el punto en x, el angulo, velocidad y color y hace un llamado a la
% funcion de trayectoria
for ii=1:n
    init_x = (diameter/2 * -1) + diameter*rand(1,1);
    angle = randi([35,145],1);
    velocity = randi([1,50],1);
    m = randi([30 50]);
    b = randi([10 10]); 
    color(ii,1) = rand(1,1); color(ii,2) = rand(1,1); color(ii,3) = rand(1,1);
    tabla{ii} = trajectoryfunc(angle, velocity, height, init_x, dt,m,b,g);
end

% Graficar
title("Reto F1004B");
xlabel("Desplazamiento en X");
ylabel("Desplazamiento en Y");
hold on;
trapecio = polyshape([-diameter/2 * 5 -diameter/2 diameter/2 diameter/2 * 5], [0 height height 0]);
plot(trapecio);

 for j = 1:length(tabla{1})-1
     for l = 1:n
         if j >= (tabla{l}(1,3))/dt
               x = tabla{l}(j+1 - (tabla{l}(1,3))/dt,1);
               y = tabla{l}(j+1 - (tabla{l}(1,3))/dt,2);
               % disp( ['x: ' num2str(x) ', y: ' num2str(y) ', j: ' num2str(j) ', l: ' num2str(l)]);
               plot(x,y, '.', 'color', color(l,1:3));
               pause(0.05);
         end
     end
 end
 
% Genera tabla de analisis
analisis = zeros(n,9);
for ii = 1:n
    if max(tabla{ii}(:,3)) ~= 0
        [analisis(ii,1), index] = max(tabla{ii}(:,2));
        analisis(ii,2) = min(tabla{ii}(:,3));
        analisis(ii,3) = tabla{ii}(index,3);
        analisis(ii,4) = tabla{ii}(index+1,3);
        analisis(ii,5) = max(tabla{ii}(:,3));
        analisis(ii,7) = max(tabla{ii}(:,3));
        analisis(ii,8) = max(tabla{ii}(:,2));
        analisis(ii,9) = max(tabla{ii}(:,1));
    else
        analisis(ii,1) = max(tabla{ii}(:,2));
        analisis(ii,8) = max(tabla{ii}(:,2));
        analisis(ii,9) = max(tabla{ii}(:,1));
    end
end
% Convierte matriz a tabla
analisis_tabla = array2table(analisis, 'VariableNames', {'Punto critico', 'Inicio Creciente (en segundos)', 'Final Creciente (en segundos)', 'Inicio Decreciente (en segundos)', 'Final Decreciente (en segundos)', 'Inicio Concavidad Negativa (en segundos)', 'Final Concavidad Negativa (en segundos)', 'Altura Maxima', 'Desplazamiento Maximo'});
% Imprime la tabla
disp(analisis_tabla);

% Funcion para calcular la trayectoria
function trajectory = trajectoryfunc(angle,velocity, y_disp, x_disp, dt,m,b,g)
    ti = 0:dt:15; % Tiempo
    n = length(ti); % longitud del tiempo, funciona como el indice
    pos_x = zeros(n,1); % Matriz de posicion en x
    pos_y = zeros(n,1); % Matriz de posicion en y
    vx = zeros(n,1); % Matriz de velocidad en x
    vy = zeros(n,1); % Matriz de velocidad en y
    vx(1) = velocity.*cosd(angle); % Velocidad inicial x
    vy(1) = velocity.*sind(angle); % Velocidad inicial y
    ax = zeros(n,1); % Vector de aceleracion en x
    ay = zeros(n,1); % Vector de aceleracion en y
    pos_x(1) = x_disp; % Define la posicion inicial en X, igual al desplazamiento en x (parametro x_disp)
    pos_y(1) = y_disp; % Define la posicion inicial en Y, igual al desplazamiento en y (parametro y_disp)
    
    trajectory = zeros(n,3); % Matriz resultante con las posiciones en x, en y, y el tiempo
    trajectory(:,3) = 0:dt:15; % Escribe en la tercera columna el tiempo
    trajectory(1,1) = x_disp; % Define la posicion inicial en X, igual al desplazamiento en x (parametro x_disp)
    trajectory(1,2) = y_disp; % Define la posicion inicial en Y, igual al desplazamiento en y (parametro y_disp)

    for ii = 2:n
         ax(ii-1) = -b/m*vx(ii-1);
         ay(ii-1) = g-b/m*vy(ii-1);
         vx(ii) = vx(ii-1) + dt*ax(ii-1);
         vy(ii) = vy(ii-1) + dt*ay(ii-1);
         pos_x(ii) = pos_x(ii-1) + vx(ii-1) * dt;
         pos_y(ii) = pos_y(ii-1) + vy(ii-1) * dt;
         trajectory(ii,1) = pos_x(ii);
         trajectory(ii,2) = pos_y(ii);
    end
    trajectory(:,3) = trajectory(:,3) + randi([0,4],1);
end
