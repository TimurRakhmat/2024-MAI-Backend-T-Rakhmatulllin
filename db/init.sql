create table VisitorProfile(
	login VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255) NOT NULL
);

create table Zone(
	title VARCHAR(255) PRIMARY KEY,
    description TEXT
);


create table Ticket(
	ticket_id  SERIAL PRIMARY KEY,
	date_purchase timestamp DEFAULT CURRENT_TIMESTAMP,
	duration INTEGER,
	visitor_id varchar(255),
	FOREIGN KEY (visitor_id) REFERENCES VisitorProfile (login)
);

create table TicketZone(
	ticket_id int,
	zone_id VARCHAR(255),
	FOREIGN KEY (ticket_id) REFERENCES Ticket(ticket_id),
    FOREIGN KEY (zone_id) REFERENCES Zone(title),
	PRIMARY KEY (ticket_id, zone_id)
);