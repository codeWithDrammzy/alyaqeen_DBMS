 <div class="header">
            <div class="header-left flex items-center gap-4">
               <a href="index.html" class="logo">
                  <img src="{% static 'assets/images/logo1.jpg' %}" alt="Logo">
               </a>
               
            </div>


            <a href="javascript:void(0);" id="toggle_btn">
            <i class="fas fa-align-left"></i>
            </a>
            <div class="top-nav-search">
               <form>
                  <input type="text" class="form-control" placeholder="Search here">
                  <button class="btn" type="submit"><i class="fas fa-search"></i></button>
               </form>
            </div>
            <a class="mobile_btn" id="mobile_btn">
            <i class="fas fa-bars"></i>
            </a>
            <ul class="nav user-menu">
               <li class="nav-item dropdown noti-dropdown">
                  <a href="#" class="dropdown-toggle nav-link" data-toggle="dropdown">
                   {% if unread_notification_count > 0 %}
                  <i class="far fa-bell"></i> <span class="badge badge-pill">{{unread_notification_count}}</span>
                  {% endif %}
                  </a>
                  <div class="dropdown-menu notifications">
                     <div class="topnav-dropdown-header">
                        <span class="notification-title">Notifications</span>
                        <a href="javascript:void(0)" class="clear-noti"> Clear All </a>
                     </div>
                     <div class="noti-content">
                        <ul class="notification-list">
                           {% for notification in unread_notification %}
                           <li class="notification-message">
                              <a href="#">
                                 <div class="media">
                                    <span class="avatar avatar-sm">
                                    <img class="avatar-img rounded-circle" alt="User Image" src="assets/img/profiles/avatar-02.jpg">
                                    </span>
                                    <div class="media-body">
                                       <p class="noti-details"><span class="noti-title">{{ notification.user.username }}</span> {{ notification.message }} <span class="noti-title">your estimate</span></p>
                                       <p class="noti-time"><span class="notification-time">{{ notification.created_at|timesince }} ago</span></p>
                                    </div>
                                 </div>
                              </a>
                           </li>
                           {% endfor %}

                        </ul>
                     </div>
                     <div class="topnav-dropdown-footer">
                        <a href="#">View all Notifications</a>
                     </div>
                  </div>
                  
               </li>
               <li class="nav-item dropdown has-arrow">
                  <a href="#" class="dropdown-toggle nav-link" data-toggle="dropdown">
                     <span class="user-img">
                       {{user.email}}
                     </span>
                  </a>

                  <div class="dropdown-menu">
                     <div class="user-header">
                        
                        <div class="user-text">
                           <h6>{{user.first_name}}</h6>
                           <p class="text-muted mb-0">Administrator</p>
                        </div>
                     </div>
                     <a class="dropdown-item" href="profile.html">My Profile</a>
                     <a class="dropdown-item" href="inbox.html">Inbox</a>
                     <a class="dropdown-item" href="{% url 'logout-user' %}">Logout</a>
                  </div>
               </li>
            </ul>
         </div>