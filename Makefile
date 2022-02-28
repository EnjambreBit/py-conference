DB_NOMBRE_DEL_DUMP= ~/Dropbox/Trabajo/Conference/backups/conference_backup_`date +'%Y%m%d_%Hhs%Mmin'`.dump
DB_DUMP_MAS_RECIENTE=`ls -Art ~/Dropbox/Trabajo/Conference/backups/conference_backup*.dump  | tail -n 1`
NOMBRE_BD=conference

N=[0m
R=[00;31m
G=[01;32m
Y=[01;33m
B=[01;34m
L=[01;30m

comandos:
	@echo ""
	@echo "	${B}COMANDOS DISPONIBLES"
	@echo ""
	@echo "	${G}iniciar${N}:             Instalar dependencias"
	@echo "	${G}ejecutar${N}:            Correr servidor de pruebas"
	@echo "	${G}crear_migraciones${N}:   Crear migraciones"
	@echo "	${G}migrar${N}:              Ejecutar migraciones pendientes"
	@echo "	${G}reset${N}:               Resetear base de datos"
	@echo "	${G}collectstatic${N}"
	@echo "	${G}realizar_backup${N}:     Realizar backup de la base de datos"
	@echo "	${G}cargar_ultimo_dump${N}:  Cargar ultimo backup"
	@echo "	${G}blacked${N}:             Unificar estilo de codigo"
	@echo ""

iniciar:
	@pipenv install

ejecutar:
	@pipenv run python manage.py runserver

crear_migraciones:
	@pipenv run python manage.py makemigrations

migrar:
	@pipenv run python manage.py migrate --noinput

reset:
	dropdb --if-exists ${NOMBRE_BD} -e; createdb ${NOMBRE_BD}
	pipenv run python manage.py migrate --noinput

collectstatic:
	pipenv run python manage.py collectstatic

realizar_backup:
	@echo "Creando el archivo ${DB_NOMBRE_DEL_DUMP}"
	@pg_dump -F c ${NOMBRE_BD} > ${DB_NOMBRE_DEL_DUMP}

cargar_ultimo_dump:
	@echo "Se cargará el dump mas reciente: ${DB_DUMP_MAS_RECIENTE}"
	dropdb --if-exists ${NOMBRE_BD} -e; createdb ${NOMBRE_BD}
	pg_restore --no-acl --no-owner -d ${NOMBRE_BD} ${DB_DUMP_MAS_RECIENTE}
	@make migrar

blacked:
	@echo pipenv run python black .