<div class="flex justify-center  items-center bg-gray-50 ">
    <div class="relative w-[420px] h-[260px] bg-white border border-gray-200 rounded-xl shadow-2xl overflow-hidden transform hover:scale-105 transition-transform duration-300">

        <div class="bg-blue-800 text-white text-center text-xs py-1 px-3 font-medium tracking-wide">
            No. 7 Al-Yaqeen Road, Behind Water Board Building, Malali Layout, Kaduna.
                </div>

            <div class="absolute inset-0 z-0 flex items-center justify-center">
            <img src="{% static 'assets/images/logo1.jpg' %}" alt="School Logo"
                class="w-72 h-72 object-contain opacity-10">
        </div>


        <div class="relative z-10 flex h-[calc(100%-2.5rem)] p-4 gap-5 items-center">

            <div class="flex-shrink-0 flex items-center justify-center">
                {% if staff.avatar %}
                    <img src="{{ staff.avatar.url }}" alt="Avatar"
                        class="h-28 w-28 rounded-full object-cover border-4 border-white shadow-lg ring-2 ring-blue-500">
                {% else %}
                    <div class="h-28 w-28 rounded-full bg-blue-600 text-white flex items-center justify-center text-4xl font-bold shadow-lg">
                        {{ staff.first_name|first|upper }}{{ staff.last_name|first|upper }}
                    </div>
                {% endif %}
            </div>

            <div class="flex flex-col justify-center text-sm text-gray-800 w-full">
                <div>
                    <h2 class="text-2xl font-extrabold text-blue-900 leading-tight">
                        {{ staff.first_name|upper }} {{ staff.last_name|upper }}
                    </h2>
                    <p class="text-sm italic text-gray-600 mt-0.5">{{ staff.role|title }}</p>
                </div>

                <div class="mt-4 space-y-1.5">
                    <p class="flex items-center"><span class="font-semibold text-gray-700 w-16">ID:</span> <span class="ml-1 font-medium text-blue-700">{{ staff.staff_id }}</span></p>
                    <p class="flex items-center"><span class="font-semibold text-gray-700 w-16">Email:</span> <span class="ml-1">{{ staff.user.email }}</span></p>
                    <p class="flex items-center"><span class="font-semibold text-gray-700 w-16">Phone:</span> <span class="ml-1">{{ staff.phone }}</span></p>
                    <p class="flex items-center"><span class="font-semibold text-gray-700 w-16">Joined:</span> <span class="ml-1">{{ staff.date_joined }}</span></p>
                </div>
            </div>
        </div>

        <div class="absolute bottom-0 left-0 right-0 bg-blue-700 text-white text-[10px] py-1 px-3 text-center font-semibold z-10">
            AYQ School Management System
        </div>
    </div>
</div>