# Industrial Communication
Overview:
- Ethernet normal vs industrial
- Ethernet based ICS  protocols
- Security considerations for commonly used protocols
- Some wireshark

## Industrial vs Traditional Ethernet
Key differences:
- Environmental Requirements
	- Industrial:
		- Temperature
		- Vibrations
		- EMC/noise
		- Chemicals
	- Hardware adaptions:
		- Rugged
		- No moving parts (like fans)
		- Low power (<= 24V)
- Installation Requirements
	- Topologies:
		- Office (Tree/Star)
		- Industrial (Bus - linear & ring - often redundant)
	- Connections:
		- Office:
			- Pre-assembled device connection cables, variable device connections
		- Industrial:
			- Needs are higher, so need to be even made much harder
- Performance Requirements
	- Packets:
		- Office:
			- Large volume data packets
		- Industrial:
			- Small data packets
	- Network:
		- Office:
			- medium network availability, transmissions timed in seconds
			- no isochronism
		- Industrial:
			- high availability, transmission timed in microseconds
			- isochronism 

## Modbus (TCP 502)
Super widely used and well-known, open standard.
It has a lot of variants as well.
It has a lot of use cases.

How it works:
- Master / slave
- Request / reply
- Three distinct units in the protocol:
	- Modbus request
	- Modbus response
	- Modbus exception response
- Security aspect
	- Concerns
		- Lack of authentication

### Exercise
- Find the IP of Master? (141.81.0.10)
> To find it, it is usually the very first IP address initialization that happens. In this case I can see it says "Query"
- How many slaves are on the network? (13)
> To find this easily, either take a look at "Query" and then see amount of machines and count them. Or, go to Статистика > Конечные точки
- What is the status of the outputs of the slave with the highest IP in the network? (0,1,0,0,0,0,0,0,0,0)
> To check this, find the "Response" package, and then at the very bottom can see the response in bits. There is like 0 and 1 combination
- Filter out all the Modbus write requests (coils and registers). How many are there?
> Here need to find the needed functions, and then filter them out.


## Profinet
Security Aspect:
- Concerns:
	- No authentication
	- No encryption
- Recommendations:
	- Careful implementation of zones and conduits

## S7comm

